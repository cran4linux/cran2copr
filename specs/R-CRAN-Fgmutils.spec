%global __brp_check_rpaths %{nil}
%global packname  Fgmutils
%global packver   0.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          3%{?dist}%{?buildtag}
Summary:          Forest Growth Model Utilities

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-tcltk 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-devEMF 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-data.table 
Requires:         R-tcltk 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-devEMF 
Requires:         R-CRAN-png 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
Growth models and forest production require existing data manipulation and
the creation of new data, structured from basic forest inventory data. The
purpose of this package is provide functions to support these activities.

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
