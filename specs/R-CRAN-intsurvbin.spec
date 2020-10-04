%global packname  intsurvbin
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Survival and Binary Data Integration

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.1
Requires:         R-core >= 2.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MHadaptive 
BuildRequires:    R-mgcv 
Requires:         R-CRAN-msm 
Requires:         R-stats 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MHadaptive 
Requires:         R-mgcv 

%description
Function to implement the horseshoe shrinkage prior in integrated survival
and binary regression as developed in Maity et. al. (2019)
<doi:10.1111/rssc.12377>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
