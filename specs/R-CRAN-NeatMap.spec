%global packname  NeatMap
%global packver   0.3.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6.2
Release:          2%{?dist}
Summary:          Non-clustered heatmap alternatives

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgl 

%description
NeatMap is a package to create heatmap like plots in 2 and 3 dimensions,
without the need for cluster analysis. Like the heatmap, the plots created
by NeatMap display both a dimensionally reduced representation of the data
as well as the data itself. They are intended to be used in conjunction
with dimensional reduction techniques such as PCA.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
