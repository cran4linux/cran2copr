%global packname  ggupset
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Combination Matrix Axis for 'ggplot2' to Create 'UpSet' Plots

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-gtable 
Requires:         R-grid 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 

%description
Replace the standard x-axis in 'ggplots' with a combination matrix to
visualize complex set overlaps. 'UpSet' has introduced a new way to
visualize the overlap of sets as an alternative to Venn diagrams. This
package provides a simple way to produce such plots using 'ggplot2'. In
addition it can convert any categorical axis into a combination matrix
axis.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
