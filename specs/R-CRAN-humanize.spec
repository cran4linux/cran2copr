%global __brp_check_rpaths %{nil}
%global packname  humanize
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Create Values for Human Consumption

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-glue 

%description
An almost direct port of the 'python' 'humanize' package
<https://github.com/jmoiron/humanize>. This package contains utilities to
convert values into human readable forms.

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
