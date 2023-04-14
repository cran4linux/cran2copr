%global __brp_check_rpaths %{nil}
%global packname  rIntervalTree
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          An Interval Tree Tool for Real Numbers

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
This tool can be used to build binary interval trees using real number
inputs. The tree supports queries of intervals overlapping a single number
or an interval (start, end). Intervals with same bounds but different
names are treated as distinct intervals. Insertion of intervals is also
allowed. Deletion of intervals is not implemented at this point. See Mark
de Berg, Otfried Cheong, Marc van Kreveld, Mark Overmars (2008).
Computational Geometry: Algorithms and Applications, for a reference.

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
