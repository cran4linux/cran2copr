%global packname  ROI.plugin.glpk
%global packver   0.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          'ROI' Plug-in 'GLPK'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rglpk >= 0.6.2
BuildRequires:    R-CRAN-ROI >= 0.3.0
BuildRequires:    R-methods 
Requires:         R-CRAN-Rglpk >= 0.6.2
Requires:         R-CRAN-ROI >= 0.3.0
Requires:         R-methods 

%description
Enhances the 'R' Optimization Infrastructure ('ROI') package by
registering the free 'GLPK' solver. It allows for solving mixed integer
linear programming ('MILP') problems as well as all variants/combinations
of 'LP', 'IP'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
