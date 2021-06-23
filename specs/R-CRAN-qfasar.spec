%global __brp_check_rpaths %{nil}
%global packname  qfasar
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Quantitative Fatty Acid Signature Analysis in R

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp >= 1.16
Requires:         R-CRAN-Rsolnp >= 1.16

%description
An implementation of Quantitative Fatty Acid Signature Analysis (QFASA) in
R.  QFASA is a method of estimating the diet composition of predators.
The fundamental unit of information in QFASA is a fatty acid signature
(signature), which is a vector of proportions describing the composition
of fatty acids within lipids. Signature data from at least one predator
and from samples of all potential prey types are required.  Calibration
coefficients, which adjust for the differential metabolism of individual
fatty acids by predators, are also required. Given those data inputs, a
predator signature is modeled as a mixture of prey signatures and its diet
estimate is obtained as the mixture that minimizes a measure of distance
between the observed and modeled signatures.  A variety of estimation
options and simulation capabilities are implemented. Please refer to the
vignette for additional details and references.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
