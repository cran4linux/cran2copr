%global packname  IgorR
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}
Summary:          Read Binary Files Saved by 'Igor Pro' (Including 'Neuromatic'Data)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-tools 
Requires:         R-CRAN-bitops 
Requires:         R-tools 

%description
Provides function to read data from the 'Igor Pro' data analysis program
by Wavemetrics. The data formats supported are 'Igor' packed experiment
format (pxp) and 'Igor' binary wave (ibw). See:
http://www.wavemetrics.com/ for details. Also includes functions to load
special pxp files produced by the 'Igor Pro' 'Neuromatic' and 'Nclamp'
packages for recording and analysing neuronal data. See
http://www.neuromatic.thinkrandom.com/ for details.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/igor
%{rlibdir}/%{packname}/INDEX
