%global __brp_check_rpaths %{nil}
%global packname  unjoin
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Separate a Data Frame by Normalization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Separate a data frame in two based on key columns. The function unjoin()
provides an inside-out version of a nested data frame. This is used to
identify duplication and normalize it (in the database sense) by linking
two tables with the redundancy removed. This is a basic requirement for
detecting topology within spatial structures that has motivated the need
for this package as a building block for workflows within more applied
projects.

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
%{rlibdir}/%{packname}
