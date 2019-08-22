%global packname  biogas
%global packver   1.10.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10.3
Release:          1%{?dist}
Summary:          Process Biogas Data and Predict Biogas Production

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
High- and low-level functions for processing biogas data and predicting
biogas production. Molar mass and calculated oxygen demand (COD') can be
determined from a chemical formula. Measured gas volume can be corrected
for water vapor and to (possibly user-defined) standard temperature and
pressure. Gas quantity can be converted between volume, mass, and moles.
Gas composition, cumulative production, or other variables can be
interpolated to a specified time. Cumulative biogas and methane production
(and rates) can be calculated using volumetric, manometric, or gravimetric
methods for any number of reactors. With cumulative methane production
data and data on reactor contents, biochemical methane potential (BMP) can
be calculated and summarized, including subtraction of the inoculum
contribution and normalization by substrate mass. Cumulative production
and production rates can be summarized in several different ways (e.g.,
omitting normalization) using the same function. Biogas quantity and
composition can be predicted from substrate composition and additional,
optional data. Lastly, inoculum and substrate mass can be determined for
planning BMP experiments.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
