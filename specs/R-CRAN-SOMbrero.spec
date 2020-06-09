%global packname  SOMbrero
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          SOM Bound to Realize Euclidean and Relational Outputs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 1.0
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggwordcloud 
BuildRequires:    R-CRAN-metR 
BuildRequires:    R-CRAN-interp 
Requires:         R-CRAN-igraph >= 1.0
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-shiny 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggwordcloud 
Requires:         R-CRAN-metR 
Requires:         R-CRAN-interp 

%description
The stochastic (also called on-line) version of the Self-Organising Map
(SOM) algorithm is provided. Different versions of the algorithm are
implemented, for numeric and relational data and for contingency tables as
described, respectively, in Kohonen (2001) <isbn:3-540-67921-9>, Olteanu &
Villa-Vialaneix (2005) <doi:10.1016/j.neucom.2013.11.047> and Cottrell et
al (2004) <doi:10.1016/j.neunet.2004.07.010>. The package also contains
many plotting features (to help the user interpret the results) and a
graphical user interface based on 'shiny'.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
