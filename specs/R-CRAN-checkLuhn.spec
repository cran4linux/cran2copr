%global __brp_check_rpaths %{nil}
%global packname  checkLuhn
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Checks if a Number is Valid Using the Luhn Algorithm

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 

%description
Confirms if the number is Luhn compliant. Can check if credit card, IMEI
number or any other Luhn based number is correct. For more info see:
<https://en.wikipedia.org/wiki/Luhn_algorithm>.

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
