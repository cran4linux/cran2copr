%global __brp_check_rpaths %{nil}
%global packname  Mondrian
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Simple Graphical Representation of the Relative Occurrence andCo-Occurrence of Events

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-RColorBrewer 

%description
The unique function of this package allows representing in a single graph
the relative occurrence and co-occurrence of events measured in a sample.
As examples, the package was applied to describe the occurrence and
co-occurrence of different species of bacterial or viral symbionts
infecting arthropods at the individual level. The graphics allows
determining the prevalence of each symbiont and the patterns of multiple
infections (i.e. how different symbionts share or not the same individual
hosts). We named the package after the famous painter as the graphical
output recalls Mondrian’s paintings.

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
%{rlibdir}/%{packname}
