%global packname  fastNaiveBayes
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Extremely Fast Implementation of a Naive Bayes Classifier

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
Requires:         R-Matrix 
Requires:         R-stats 

%description
This is an extremely fast implementation of a Naive Bayes classifier. This
package is currently the only package that supports a Bernoulli
distribution, a Multinomial distribution, and a Gaussian distribution,
making it suitable for both binary features, frequency counts, and
numerical features. Another feature is the support of a mix of different
event models. Only numerical variables are allowed, however, categorical
variables can be transformed into dummies and used with the Bernoulli
distribution. The implementation is largely based on the paper "A
comparison of event models for Naive Bayes anti-spam e-mail filtering"
written by K.M. Schneider (2003) <doi:10.3115/1067807.1067848>. Any issues
can be submitted to: <https://github.com/mskogholt/fastNaiveBayes/issues>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
