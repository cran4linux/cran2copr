%global packname  stoRy
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Functions for the Analysis of Star Trek Thematic Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-data.tree 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-data.tree 

%description
An implementation of 1) the hypergeometric test for over-representation of
literary themes in a storyset (a list of stories) relative to a background
list of stories, and 2) a recommendation system that takes a user-selected
story as input and returns a ranked list of similar stories on the basis
of shared themes. The package is currently implemented for the episodes of
the Star Trek television franchise series The Original Series (TOS), The
Animated Series (TAS), The Next Generation (TNG), and Voyager (VOY).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/datasets
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/storysets
%{rlibdir}/%{packname}/INDEX
