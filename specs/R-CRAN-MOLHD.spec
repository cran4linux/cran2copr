%global debug_package %{nil}
%global packname  MOLHD
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          2%{?dist}
Summary:          Multiple Objective Latin Hypercube Design

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-arrangements 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-arrangements 

%description
Generate the optimal maximin distance, minimax distance (only for low
dimensions), and maximum projection designs within the class of Latin
hypercube designs efficiently for computer experiments. Generate Pareto
front optimal designs for each two of the three criteria and all the three
criteria within the class of Latin hypercube designs efficiently. Provide
criterion computing functions. References of this package can be found in
Morris, M. D. and Mitchell, T. J. (1995)
<doi:10.1016/0378-3758(94)00035-T>, Lu Lu and Christine M.
Anderson-CookTimothy J. Robinson (2011) <doi:10.1198/Tech.2011.10087>,
Joseph, V. R., Gul, E., and Ba, S. (2015) <doi:10.1093/biomet/asv002>.

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
%{rlibdir}/%{packname}/INDEX
