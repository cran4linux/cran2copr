%global packname  enrichwith
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          Methods to Enrich R Objects with Extra Components

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch

%description
Provides the "enrich" method to enrich list-like R objects with new,
relevant components. The current version has methods for enriching objects
of class 'family', 'link-glm', 'lm', 'glm' and 'betareg'. The resulting
objects preserve their class, so all methods associated with them still
apply. The package also provides the 'enriched_glm' function that has the
same interface as 'glm' but results in objects of class 'enriched_glm'. In
addition to the usual components in a `glm` object, 'enriched_glm' objects
carry an object-specific simulate method and functions to compute the
scores, the observed and expected information matrix, the first-order
bias, as well as model densities, probabilities, and quantiles at
arbitrary parameter values. The package can also be used to produce
customizable source code templates for the structured implementation of
methods to compute new components and enrich arbitrary objects.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/dev_resids.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
