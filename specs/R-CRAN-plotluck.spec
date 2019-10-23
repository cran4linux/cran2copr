%global packname  plotluck
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          'ggplot2' Version of "I'm Feeling Lucky!"

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.26
BuildRequires:    R-CRAN-Hmisc >= 3.17.4
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-hexbin >= 1.27.1
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-scales >= 0.4.1
BuildRequires:    R-grid 
Requires:         R-CRAN-quantreg >= 5.26
Requires:         R-CRAN-Hmisc >= 3.17.4
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-hexbin >= 1.27.1
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-scales >= 0.4.1
Requires:         R-grid 

%description
Examines the characteristics of a data frame and a formula to
automatically choose the most suitable type of plot out of the following
supported options: scatter, violin, box, bar, density, hexagon bin, spine
plot, and heat map. The aim of the package is to let the user focus on
what to plot, rather than on the "how" during exploratory data analysis.
It also automates handling of observation weights, logarithmic axis
scaling, reordering of factor levels, and overlaying smoothing curves and
median lines. Plots are drawn using 'ggplot2'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/image
%{rlibdir}/%{packname}/INDEX
