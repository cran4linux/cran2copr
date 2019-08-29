%global packname  ICEinfer
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Incremental Cost-Effectiveness Inference using Two UnbiasedSamples

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-lattice 
Requires:         R-lattice 

%description
Given two unbiased samples of patient level data on cost and effectiveness
for a pair of treatments, make head-to-head treatment comparisons by (i)
generating the bivariate bootstrap resampling distribution of ICE
uncertainty for a specified value of the shadow price of health, lambda,
(ii) form the wedge-shaped ICE confidence region with specified confidence
fraction within [0.50, 0.99] that is equivariant with respect to changes
in lambda, (iii) color the bootstrap outcomes within the above confidence
wedge with economic preferences from an ICE map with specified values of
lambda, beta and gamma parameters, (iv) display VAGR and ALICE
acceptability curves, and (v) illustrate variation in ICE preferences by
displaying potentially non-linear indifference(iso-preference) curves from
an ICE map with specified values of lambda, beta and either gamma or eta
parameters.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
