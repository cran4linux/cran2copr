%global __brp_check_rpaths %{nil}
%global packname  qqvases
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Animated Normal Quantile-Quantile Plots

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-stats 
Requires:         R-graphics 

%description
Presents an explanatory animation of normal quantile-quantile plots based
on a water-filling analogy.  The animation presents a normal QQ plot as
the parametric plot of the water levels in vases defined by two
distributions.  The distributions decorate the axes in the normal QQ plot
and are optionally shown as vases adjacent to the plot.  The package draws
QQ plots for several distributions, either as samples or continuous
functions.

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
