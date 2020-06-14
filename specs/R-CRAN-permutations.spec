%global packname  permutations
%global packver   1.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          2%{?dist}
Summary:          The Symmetric Group: Permutations of a Finite Set

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-partitions >= 1.9.17
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-numbers 
Requires:         R-CRAN-partitions >= 1.9.17
Requires:         R-CRAN-magic 
Requires:         R-CRAN-numbers 

%description
Manipulates invertible functions from a finite set to itself.  Can
transform from word form to cycle form and back.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/code.R
%doc %{rlibdir}/%{packname}/code2.R
%{rlibdir}/%{packname}/data.txt
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/dodecahedron_group.py
%doc %{rlibdir}/%{packname}/full_dodecahedron_group.py
%doc %{rlibdir}/%{packname}/guide.R
%doc %{rlibdir}/%{packname}/megaminx_net_guides.svg
%doc %{rlibdir}/%{packname}/megaminx.py
%doc %{rlibdir}/%{packname}/megaminx.R
%doc %{rlibdir}/%{packname}/net_coords.txt
%doc %{rlibdir}/%{packname}/order_of_ops.Rmd
%doc %{rlibdir}/%{packname}/read.me
%doc %{rlibdir}/%{packname}/representation.Rmd
%doc %{rlibdir}/%{packname}/starminx_III.py
%doc %{rlibdir}/%{packname}/starminx.py
%{rlibdir}/%{packname}/INDEX
