%global packname  OutliersO3
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          3%{?dist}%{?buildtag}
Summary:          Draws Overview of Outliers (O3) Plots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cellWise >= 2.1.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-HDoutliers 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-robustX 
BuildRequires:    R-CRAN-FastPCS 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-memisc 
Requires:         R-CRAN-cellWise >= 2.1.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-HDoutliers 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-robustX 
Requires:         R-CRAN-FastPCS 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-memisc 

%description
Potential outliers are identified for all combinations of a dataset's
variables. O3 plots are described in Unwin(2019)
<doi:10.1080/10618600.2019.1575226>. The available methods are
HDoutliers() from the package 'HDoutliers', FastPCS() from the package
'FastPCS', mvBACON() from 'robustX', adjOutlyingness() from 'robustbase',
DectectDeviatingCells() from 'cellWise', covMcd() from 'robustbase'.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
