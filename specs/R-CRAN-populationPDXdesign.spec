%global __brp_check_rpaths %{nil}
%global packname  populationPDXdesign
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Designing Population PDX Studies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 

%description
Run simulations to assess the impact of various designs features and the
underlying biological behaviour on the outcome of a Patient Derived
Xenograft (PDX) population study. This project can either be deployed to a
server as a 'shiny' app or installed locally as a package and run the app
using the command 'populationPDXdesignApp()'.

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
