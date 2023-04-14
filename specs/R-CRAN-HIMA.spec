%global __brp_check_rpaths %{nil}
%global packname  HIMA
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          3%{?dist}%{?buildtag}
Summary:          High-Dimensional Mediation Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-ncvreg 
Requires:         R-stats 
Requires:         R-CRAN-iterators 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Allows to estimate and test high-dimensional mediation effects based on
sure independent screening and minimax concave penalty techniques. A joint
significance test is used for mediation effect. Haixiang Zhang, Yinan
Zheng, Zhou Zhang, Tao Gao, Brian Joyce, Grace Yoon, Wei Zhang, Joel
Schwartz, Allan Just, Elena Colicino, Pantel Vokonas, Lihui Zhao, Jinchi
Lv, Andrea Baccarelli, Lifang Hou, Lei Liu (2016)
<doi:10.1093/bioinformatics/btw351>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
