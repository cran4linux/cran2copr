%global packname  bbw
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          Blocked Weighted Bootstrap

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-car 

%description
The blocked weighted bootstrap (BBW) is an estimation technique for use
with data from two-stage cluster sampled surveys in which either prior
weighting (e.g. population-proportional sampling or PPS as used in
Standardized Monitoring and Assessment of Relief and Transitions or SMART
surveys) or posterior weighting (e.g. as used in rapid assessment method
or RAM and simple spatial sampling method or S3M surveys). The method was
developed by Accion Contra la Faim, Brixton Health, Concern Worldwide,
Global Alliance for Improved Nutrition, UNICEF Sierra Leone, UNICEF Sudan
and Valid International. It has been tested by the Centers for Disease
Control (CDC) using infant and young child feeding (IYCF) data. See
Cameron et al (2008) <doi:10.1162/rest.90.3.414> for application of
bootstrap to cluster samples. See Aaron et al (2016)
<doi:10.1371/journal.pone.0163176> and Aaron et al (2016)
<doi:10.1371/journal.pone.0162462> for application of the blocked weighted
bootstrap to estimate indicators from two-stage cluster sampled surveys.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
