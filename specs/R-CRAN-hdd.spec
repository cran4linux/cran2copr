%global __brp_check_rpaths %{nil}
%global packname  hdd
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Easy Manipulation of Out of Memory Data Sets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fst 
Requires:         R-utils 
Requires:         R-CRAN-readr 

%description
Hard drive data: Class of data allowing the easy importation/manipulation
of out of memory data sets. The data sets are located on disk but look
like in-memory, the syntax for manipulation is similar to 'data.table'.
Operations are performed "chunk-wise" behind the scene.

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
