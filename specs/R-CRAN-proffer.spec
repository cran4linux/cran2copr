%global packname  proffer
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Profile R Code and Visualize with 'Pprof'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-profile 
BuildRequires:    R-CRAN-RProtoBuf 
BuildRequires:    R-utils 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-profile 
Requires:         R-CRAN-RProtoBuf 
Requires:         R-utils 

%description
Like similar profiling tools, the 'proffer' package automatically detects
sources of slowness in R code. The distinguishing feature of 'proffer' is
its utilization of 'pprof', which supplies interactive visualizations that
are efficient and easy to interpret. Behind the scenes, the 'profile'
package converts native 'Rprof()' data to a protocol buffer that 'pprof'
understands. For the documentation of 'proffer', visit
<https://r-prof.github.io/proffer>. To learn about the implementations and
methodologies of 'pprof', 'profile', and protocol buffers, visit
<https://github.com/google/pprof>.
<https://developers.google.com/protocol-buffers>, and
<https://github.com/r-prof/profile>, respectively.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
