%global __brp_check_rpaths %{nil}
%global packname  bender
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bender Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 

%description
R client for Bender Hyperparameters optimizer : <https://bender.dreem.com>
The R client allows you to communicate with the Bender API and therefore
submit some new trials within your R script itself.

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
