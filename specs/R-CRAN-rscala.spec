%global __brp_check_rpaths %{nil}
%global packname  rscala
%global packver   3.2.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.19
Release:          3%{?dist}%{?buildtag}
Summary:          Bridge Between 'R' and 'Scala' with Callbacks

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz
Source1:          https://downloads.lightbend.com/scala/2.12.8/scala-2.12.8.tgz
Source2:          https://github.com/sbt/sbt/releases/download/v1.2.8/sbt-1.2.8.tgz

BuildRequires:    java
Requires:         java
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
'Scala' <http://www.scala-lang.org/> is embedded in 'R' and callbacks from
'Scala' to 'R' are available. Support is provided to write 'R' packages
that access 'Scala'. After installation, please run
'rscala::scalaConfig()'.  The vignette provides an update of the original
paper <doi:10.18637/jss.v092.i04>.

%prep
%setup -q -c -n %{packname} -a 1 -a 2
mkdir %{packname}/inst/dependencies
mv scala* %{packname}/inst/dependencies/scala
mv sbt* %{packname}/inst/dependencies/sbt
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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHT
%{rlibdir}/%{packname}/data-raw
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
%doc %{rlibdir}/%{packname}/dependencies
