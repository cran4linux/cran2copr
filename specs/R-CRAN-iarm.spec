%global packname  iarm
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Item Analysis in Rasch Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-eRm 
BuildRequires:    R-CRAN-PP 
BuildRequires:    R-CRAN-psychotools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vcdExtra 
Requires:         R-CRAN-eRm 
Requires:         R-CRAN-PP 
Requires:         R-CRAN-psychotools 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vcdExtra 

%description
Tools to assess model fit and identify misfitting items for Rasch models
(RM) and partial credit models (PCM). Included are item fit statistics,
item-restscore association, conditional likelihood ratio tests, assessment
of measurement error, estimates of the reliability and test targeting as
described in Christensen et al. (Eds.) (2013, ISBN:978-1-84821-222-0).

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
%{rlibdir}/%{packname}/INDEX
