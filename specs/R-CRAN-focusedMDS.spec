%global packname  focusedMDS
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          3%{?dist}
Summary:          Focused, Interactive Multidimensional Scaling

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-grDevices 

%description
Takes a distance matrix and plots it as an interactive graph. One point is
focused at the center of the graph, around which all other points are
plotted in their exact distances as given in the distance matrix. All
other non-focus points are plotted as best as possible in relation to one
another. Double click on any point to choose a new focus point, and hover
over points to see their ID labels. If color label categories are given,
hover over colors in the legend to highlight only those points and click
on colors to highlight multiple groups. For more information on the
rationale and mathematical background, as well as an interactive
introduction, see <https://lea-urpa.github.io/focusedMDS.html>.

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
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
