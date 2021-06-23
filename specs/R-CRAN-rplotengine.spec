%global __brp_check_rpaths %{nil}
%global packname  rplotengine
%global packver   1.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          3%{?dist}%{?buildtag}
Summary:          R as a Plotting Engine

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.2
Requires:         R-core >= 2.6.2
BuildArch:        noarch
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-xtable 

%description
Generate basic charts either by custom applications, or from a small
script launched from the system console, or within the R console. Two
ASCII text files are necessary: (1) The graph parameters file, which name
is passed to the function 'rplotengine()'. The user can specify the
titles, choose the type of the graph, graph output formats (e.g. png,
eps), proportion of the X-axis and Y-axis, position of the legend, whether
to show or not a grid at the background, etc. (2) The data to be plotted,
which name is specified as a parameter ('data_filename') in the previous
file. This data file has a tabulated format, with a single character (e.g.
tab) between each column, and a headers line located in the first row.
Optionally, the file could include data columns for showing confidence
intervals.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/mydata.txt
%doc %{rlibdir}/%{packname}/mygraph.arg
%{rlibdir}/%{packname}/INDEX
