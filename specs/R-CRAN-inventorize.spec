%global __brp_check_rpaths %{nil}
%global packname  inventorize
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inventory Analytics, Pricing and Markdowns

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-plyr 

%description
Simulate inventory policies with and without forecasting, facilitate
inventory analysis calculations such as stock levels and re-order
points,pricing and promotions calculations. The package includes
calculations of inventory metrics, stock-out calculations and ABC analysis
calculations. The package includes revenue management techniques such as
Multi-product optimization,logit and polynomial model optimization. The
functions are referenced from : 1-Harris, Ford W. (1913). "How many parts
to make at once". Factory, The Magazine of Management. <isbn10: 135–136,
152>. 2- Nahmias, S. Production and Operations Analysis. McGraw-Hill
International Edition. <isbn: 0-07- 2231265-3. Chapter 4>. 3-Silver, E.A.,
Pyke, D.F., Peterson, R. Inventory Management and Production Planning and
Scheduling. <isbn: 978-0471119470>. 4-Ballou, R.H. Business Logistics
Management. <isbn: 978-0130661845>. Chapter 9. 5-MIT Micromasters Program.
6- Columbia University course for supply and demand analysis. 8- Price
Elasticity of Demand MATH 104,Mark Mac Lean (with assistance from Patrick
Chan) 2011W For further details or correspondence
:<www.linkedin.com/in/haythamomar>, <www.rescaleanalytics.com>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
