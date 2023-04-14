%global __brp_check_rpaths %{nil}
%global packname  readit
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Effortlessly Read Any Rectangular Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-tools >= 3.4.3
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-haven >= 1.1.1
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-readxl >= 1.0.0
Requires:         R-tools >= 3.4.3
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-haven >= 1.1.1
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-readxl >= 1.0.0

%description
Providing just one primary function, 'readit' uses a set of reasonable
heuristics to apply the appropriate reader function to the given file
path. As long as the data file has an extension, and the data is (or can
be coerced to be) rectangular, readit() can probably read it.

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
