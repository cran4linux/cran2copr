%global packname  waffle
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          3%{?dist}
Summary:          Create Waffle Chart Visualizations in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-extrafont 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-extrafont 

%description
Square pie charts (a.k.a. waffle charts) can be used to communicate parts
of a whole for categorical quantities. To emulate the percentage view of a
pie chart, a 10x10 grid should be used with each square representing 1% of
the total. Modern uses of waffle charts do not necessarily adhere to this
rule and can be created with a grid of any rectangular shape. Best
practices suggest keeping the number of categories small, just as should
be done when creating pie charts. Tools are provided to create waffle
charts as well as stitch them together, and to use glyphs for making
isotype pictograms.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/fonts
%{rlibdir}/%{packname}/INDEX
