%global __brp_check_rpaths %{nil}
%global packname  effectsizescr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Indices for Single-Case Research

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-Kendall 
Requires:         R-CRAN-Kendall 

%description
Parametric and nonparametric statistics for single-case design. Regarding
nonparametric statistics, the index suggested by Parker, Vannest, Davis
and Sauber (2011) <doi:10.1016/j.beth.2010.08.006> was included. It
combines both nonoverlap and trend to estimate the effect size of a
treatment in a single case design.

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
