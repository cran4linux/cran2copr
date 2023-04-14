%global __brp_check_rpaths %{nil}
%global packname  Information
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          3%{?dist}%{?buildtag}
Summary:          Data Exploration with Information Theory (Weight-of-Evidence andInformation Value)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-plyr 
Requires:         R-utils 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
Performs exploratory data analysis and variable screening for binary
classification models using weight-of-evidence (WOE) and information value
(IV). In order to make the package as efficient as possible, aggregations
are done in data.table and creation of WOE vectors can be distributed
across multiple cores. The package also supports exploration for uplift
models (NWOE and NIV).

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
