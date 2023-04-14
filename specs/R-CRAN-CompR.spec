%global __brp_check_rpaths %{nil}
%global packname  CompR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Paired Comparison Data Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-graphics 
Requires:         R-stats 

%description
Different tools for describing and analysing paired comparison data are
presented. Main methods are estimation of products scores according
Bradley Terry Luce model. A segmentation of the individual could be
conducted on the basis of a mixture distribution approach. The number of
classes can be tested by the use of Monte Carlo simulations. This package
deals also with multi-criteria paired comparison data.

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
