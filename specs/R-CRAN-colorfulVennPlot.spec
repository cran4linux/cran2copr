%global packname  colorfulVennPlot
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          2%{?dist}
Summary:          Plot and add custom coloring to Venn diagrams for 2-dimensional,3-dimensional and 4-dimensional data.

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grid 
Requires:         R-grid 

%description
Given 2-,3- or 4-dimensional data, plots a Venn diagram, i.e. 'crossing
circles'. The user can specify values, labels for each circle-group and
unique colors for each plotted part. Here is what it would look like for a
3-dimensional plot:
http://elliotnoma.files.wordpress.com/2011/02/venndiagram.png. To see what
the 4-dimensional plot looks like, go to
http://elliotnoma.files.wordpress.com/2013/03/4dplot.png.

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
