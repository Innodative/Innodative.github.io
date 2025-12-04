Title: Contact
Slug: contact
Status: published

I'm always interested in connecting with professionals and academics working at the intersection of technology, business, and disruption. Whether you have questions about my research, are interested in consulting services, speaking engagements, or would like to discuss emerging technology trends, I'd be happy to hear from you.

<form action="https://formspree.io/f/xgvgzabq" method="POST" class="contact-form">
  <div class="form-group">
    <label for="name">Name *</label>
    <input type="text" id="name" name="name" required>
  </div>
  
  <div class="form-group">
    <label for="email">Email *</label>
    <input type="email" id="email" name="email" required>
  </div>
  
  <div class="form-group">
    <label for="organization">Organization</label>
    <input type="text" id="organization" name="organization">
  </div>
  
  <div class="form-group">
    <label for="subject">Subject *</label>
    <select id="subject" name="subject" required>
      <option value="">Select a topic...</option>
      <option value="Consulting">Consulting Inquiry</option>
      <option value="Speaking">Speaking Engagement</option>
      <option value="Research">Research Collaboration</option>
      <option value="Media">Media/Press Inquiry</option>
      <option value="Teaching">Teaching/Academic</option>
      <option value="General">General Question</option>
    </select>
  </div>
  
  <div class="form-group">
    <label for="message">Message *</label>
    <textarea id="message" name="message" rows="8" required></textarea>
  </div>
  
  <input type="hidden" name="_subject" value="New contact from Innodative.com">
  <input type="hidden" name="_next" value="https://innodative.com/contact-thanks.html">
  
  <button type="submit" class="submit-button">Send Message</button>
</form>

<style>
.contact-form {
  max-width: 650px;
  margin: 2rem 0;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-color);
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  font-family: inherit;
  font-size: 1rem;
  background-color: var(--bg-color);
  color: var(--text-color);
  transition: border-color 0.2s ease;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
  outline: none;
  border-color: var(--link-color);
}

.form-group select {
  cursor: pointer;
}

.submit-button {
  background-color: var(--text-color);
  color: var(--bg-color);
  padding: 0.75rem 2rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  font-weight: 600;
  transition: opacity 0.2s ease;
}

.submit-button:hover {
  opacity: 0.85;
}

@media (max-width: 760px) {
  .contact-form {
    max-width: 100%;
  }
}
</style>