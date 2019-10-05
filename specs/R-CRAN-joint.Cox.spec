%global packname  joint.Cox
%global packver   3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6
Release:          1%{?dist}
Summary:          Joint Frailty-Copula Models for Tumour Progression and Death inMeta-Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
Requires:         R-survival 

%description
Perform likelihood estimation and dynamic prediction under joint
frailty-copula models for tumour progression and death in meta-analysis. A
penalized likelihood method is employed for estimating model parameters,
where the baseline hazard functions are modeled by smoothing splines. The
methods are applicable for meta-analytic data combining several studies.
The methods can analyze data having information on both terminal event
time (e.g., time-to-death) and non-terminal event time (e.g.,
time-to-tumour progression). See Emura et al. (2017)
<doi:10.1177/0962280215604510> for likelihood estimation, and Emura et al.
(2018) <doi:10.1177/0962280216688032> for dynamic prediction. More details
on these methods can also be found in a book of Emura et al. (2019)
<doi:10.1007/978-981-13-3516-7>. Survival data from ovarian cancer
patients are also available.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
