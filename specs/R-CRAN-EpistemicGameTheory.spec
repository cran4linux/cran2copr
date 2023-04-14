%global __brp_check_rpaths %{nil}
%global packname  EpistemicGameTheory
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Constructing an Epistemic Model for the Games with Two Players

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-lpSolve 
Requires:         R-stats 
Requires:         R-utils 

%description
Constructing an epistemic model such that, for every player i and for
every choice c(i) which is optimal, there is one type that expresses
common belief in rationality.

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
