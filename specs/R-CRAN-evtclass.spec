%global __brp_check_rpaths %{nil}
%global packname  evtclass
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Extreme Value Theory for Open Set Classification - GPD and GEVClassifiers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-fitdistrplus 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-fitdistrplus 

%description
Two classifiers for open set recognition and novelty detection based on
extreme value theory. The first classifier is based on the generalized
Pareto distribution (GPD) and the second classifier is based on the
generalized extreme value (GEV) distribution. For details, see Vignotto,
E., & Engelke, S. (2018) <arXiv:1808.09902>.

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
