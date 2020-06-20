%global packname  {{packname}}
%global packver   {{packver}}
%global rlibdir   /usr/local/lib/R/library

Name:             {{prefix}}%{packname}
Version:          {{version}}
Release:          1%{?dist}
Summary:          {{summary}}

License:          {{license}}
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

{{dependencies}}

%description
{{description}}

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
