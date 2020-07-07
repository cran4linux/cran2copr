%global packname  gplots
%global packver   3.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.4
Release:          2%{?dist}
Summary:          Various R Programming Tools for Plotting Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-KernSmooth 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-gdata 
Requires:         R-stats 
Requires:         R-CRAN-caTools 
Requires:         R-KernSmooth 

%description
Various R programming tools for plotting data, including: - calculating
and plotting locally smoothed summary function as ('bandplot', 'wapply'),
- enhanced versions of standard plots ('barplot2', 'boxplot2',
'heatmap.2', 'smartlegend'), - manipulating colors ('col2hex',
'colorpanel', 'redgreen', 'greenred', 'bluered', 'redblue',
'rich.colors'), - calculating and plotting two-dimensional data summaries
('ci2d', 'hist2d'), - enhanced regression diagnostic plots ('lmplot2',
'residplot'), - formula-enabled interface to 'stats::lowess' function
('lowess'), - displaying textual data in plots ('textplot', 'sinkplot'), -
plotting a matrix where each cell contains a dot whose size reflects the
relative magnitude of the elements ('balloonplot'), - plotting "Venn"
diagrams ('venn'), - displaying Open-Office style plots ('ooplot'), -
plotting multiple data on same region, with separate axes ('overplot'), -
plotting means and confidence intervals ('plotCI', 'plotmeans'), - spacing
points in an x-y plot so they don't overlap ('space').

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
