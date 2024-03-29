%global __brp_check_rpaths %{nil}
%global packname  ed50simulation
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Estimate ED50 and Its Confidence Interval

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-boot 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-boot 
Requires:         R-utils 

%description
Functions of five estimation method for ED50 (50 percent effective dose)
are provided, and they are respectively Dixon-Mood method (1948)
<doi:10.2307/2280071>, Choi's original turning point method (1990)
<doi:10.2307/2531453> and it's modified version given by us, as well as
logistic regression and isotonic regression. Besides, the package also
supports comparison between two estimation results.

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
