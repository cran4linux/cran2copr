%global __brp_check_rpaths %{nil}
%global packname  whitechapelR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Advanced Policing Techniques for the Board Game "Letters fromWhitechapel"

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-igraph 

%description
Provides a set of functions to make tracking the hidden movements of the
'Jack' player easier. By tracking every possible path Jack might have
traveled from the point of the initial murder including special movement
such as through alleyways and via carriages, the police can more
accurately narrow the field of their search. Additionally, by tracking all
possible hideouts from round to round, rounds 3 and 4 should have a vastly
reduced field of search.

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
