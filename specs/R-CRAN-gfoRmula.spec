%global packname  gfoRmula
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Parametric G-Formula

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-grDevices 
BuildRequires:    R-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-truncreg 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-grDevices 
Requires:         R-nnet 
Requires:         R-parallel 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-survival 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-truncreg 
Requires:         R-utils 

%description
Implements the parametric g-formula algorithm of Robins (1986)
<doi:10.1016/0270-0255(86)90088-6>. The g-formula can be used to estimate
the causal effects of hypothetical time-varying treatment interventions on
the mean or risk of an outcome from longitudinal data with time-varying
confounding. This package allows: 1) binary or continuous/multi-level
time-varying treatments; 2) different types of outcomes (survival or
continuous/binary end of follow-up); 3) data with competing events or
truncation by death and loss to follow-up and other types of censoring
events; 4) different options for handling competing events in the case of
survival outcomes; 5) a random measurement/visit process; 6) joint
interventions on multiple treatments; and 7) general incorporation of a
priori knowledge of the data structure.

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
%{rlibdir}/%{packname}/INDEX
