%global __brp_check_rpaths %{nil}
%global packname  LindenmayeR
%global packver   0.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.13
Release:          3%{?dist}%{?buildtag}
Summary:          Functions to Explore L-Systems (Lindenmayer Systems)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-grid 
Requires:         R-CRAN-stringr 
Requires:         R-grid 

%description
L-systems or Lindenmayer systems are parallel rewriting systems which can
be used to simulate biological forms and certain kinds of fractals.
Briefly, in an L-system a series of symbols in a string are replaced
iteratively according to rules to give a more complex string. Eventually,
the symbols are translated into turtle graphics for plotting. Wikipedia
has a very good introduction: en.wikipedia.org/wiki/L-system This package
provides basic functions for exploring L-systems.

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
