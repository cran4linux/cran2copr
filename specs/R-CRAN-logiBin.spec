%global __brp_check_rpaths %{nil}
%global packname  logiBin
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Binning Variables to Use in Logistic Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-parallel 
Requires:         R-stats 

%description
Fast binning of multiple variables using parallel processing. A summary of
all the variables binned is generated which provides the information
value, entropy, an indicator of whether the variable follows a monotonic
trend or not, etc. It supports rebinning of variables to force a monotonic
trend as well as manual binning based on pre specified cuts. The cut
points of the bins are based on conditional inference trees as implemented
in the partykit package. The conditional inference framework is described
by Hothorn T, Hornik K, Zeileis A (2006) <doi:10.1198/106186006X133933>.

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
