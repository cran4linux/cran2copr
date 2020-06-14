%global packname  inventorize
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Inventory Analytics and Cost Calculations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plotly 

%description
Facilitate inventory analysis calculations such as stock levels and
re-order points,pricing and promotions calculations. the package includes
revenue management techniques such as Multi-product optimization,logit
model optimization. the package includes calculations of inventory
metrics, stock-out calculations and ABC analysis calculations. The
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
