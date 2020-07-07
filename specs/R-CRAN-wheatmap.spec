%global packname  wheatmap
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Incrementally Build Complex Plots using Natural Semantics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-RColorBrewer 

%description
Builds complex plots, heatmaps in particular, using natural semantics.
Bigger plots can be assembled using directives such as 'LeftOf',
'RightOf', 'TopOf', and 'Beneath' and more. Other features include
clustering, dendrograms and integration with 'ggplot2' generated grid
objects. This package is particularly designed for bioinformaticians to
assemble complex plots for publication.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/gen_README.Rmd
%doc %{rlibdir}/%{packname}/README.plot1.png
%doc %{rlibdir}/%{packname}/README.plot2.png
%doc %{rlibdir}/%{packname}/tutorial.Rmd
%{rlibdir}/%{packname}/INDEX
