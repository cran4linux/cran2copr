%global packname  crseEventStudy
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          A Robust and Powerful Test of Abnormal Stock Returns inLong-Horizon Event Studies

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-sandwich 

%description
Based on Dutta et al. (2018) <doi:10.1016/j.jempfin.2018.02.004>, this
package provides their standardized test for abnormal returns in
long-horizon event studies. The methods used improve the major weaknesses
of size, power, and robustness of long-run statistical tests described in
Kothari/Warner (2007) <doi:10.1016/B978-0-444-53265-7.50015-9>. Abnormal
returns are weighted by their statistical precision (i.e., standard
deviation), resulting in abnormal standardized returns. This procedure
efficiently captures the heteroskedasticity problem. Clustering techniques
following Cameron et al. (2011) <10.1198/jbes.2010.07136> are adopted for
computing cross-sectional correlation robust standard errors. The
statistical tests in this package therefore accounts for potential biases
arising from returns' cross-sectional correlation, autocorrelation, and
volatility clustering without power loss.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
